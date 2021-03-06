import logging
from math import ceil
from platforms_graphs.util import get_class
from platforms_graphs.time_strategies import time_horizon

def get_graph_view_for(graph_name):
    if graph_name == 'LineGraphView':
        return LineGraphView()
    elif graph_name == 'BarGraphView':
        return BarGraphView()
    elif graph_name == 'AggregateBarGraph':
        return AggregateBarGraphView()
    return None

def average_aggregator(aggregator_dimension_map):
        agg_dim_sum = {}
        for dimension1, agg_dim_dict in aggregator_dimension_map.iteritems():
            curr_agg_dim_sum = 0.0
            agg_count = 0
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                for (x, y) in plot_vals:
                    if y!= None and y!= '' and y.lower() !='none':
                        agg_count += 1
                        curr_agg_dim_sum += float(y)
            agg_dim_sum[dimension1] = round((curr_agg_dim_sum / agg_count), 2) if agg_count > 0 else 0.0
        return agg_dim_sum

def median_aggregator(aggregator_dimension_map):
        agg_dim_sum = {}
        for dimension1, agg_dim_dict in aggregator_dimension_map.iteritems():
            median = 0.0
            plot_vals_array = []
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                for (x, y) in plot_vals:
                    if y and y != '' and y.lower() != 'none':
                        plot_vals_array.append((x,y))
            plot_vals_array.sort(key=lambda tup: float(tup[1]))
            if len(plot_vals_array) > 1:
                if len(plot_vals_array)%2 == 0:
                    median_idx_low = (len(plot_vals_array)/2) - 1
                    median_idx_high = median_idx_low + 1
                    median = (float(plot_vals_array[median_idx_low][1]) + float(plot_vals_array[median_idx_high][1]))/2
                else:
                    median_idx = int(ceil(len(plot_vals_array)/2))
                    median = float(plot_vals_array[median_idx][1])
            elif len(plot_vals_array) == 1:
                median = float(plot_vals_array[0][1])
            agg_dim_sum[dimension1] = round(median, 2)
        return agg_dim_sum

def blind_addition_aggregator(aggregator_dimension_map):
        agg_dim_sum = {}
        for dimension1, agg_dim_dict in aggregator_dimension_map.iteritems():
            curr_agg_dim_sum = 0.0
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                for (x, y) in plot_vals:
                    if y and y != '' and y.lower() != 'none':
                        curr_agg_dim_sum += float(y)
            agg_dim_sum[dimension1] = curr_agg_dim_sum
        return agg_dim_sum

class GraphView():
    def __init__(self):
        self.graph_model = None
        self.aggregator_strategy = None
        self.time_strategy = None
        self.time_as_dimension_strategy = None

    def get_dimension(self):
        dimension_title = self.graph_model.property_titles[self.graph_model.xaxis_id]
        ret_val = {}
        ret_val[dimension_title] = self.graph_model.filter_unique_vals
        return ret_val

    def get_values_for(self, filter_vals):
        pass

    def find_matches_in(self, plot_vals, filter_vals):
        matches = []
        for plot_val in plot_vals:
            add_co_ord = True
            co_ord = plot_val.co_ord
            model = plot_val.model
            if len(filter_vals) > 0:
                for filter_val in filter_vals:
                    idx = filter_val[0]
                    val = filter_val[1]
                    model_val = model.properties[int(idx)].value
                    f_vals = [str(v) for v in val.split(',')]
                    if model.property_titles[model.properties[int(idx)].unique_id] == 'Time':
                        model_val = self.time_strategy(model_val) if self.time_strategy else time_horizon(model_val)
                        temp_add = False
                        for v in model_val:
                            if v in f_vals:
                                temp_add = True
                        if not temp_add:
                            add_co_ord = False
                    elif model_val not in f_vals:
                        add_co_ord = False
                        break
            if add_co_ord:
                matches.append(co_ord)
        return matches

    def translate_to_json(self, filters):
        pass

class LineGraphView(GraphView):
    def get_dimension(self):
        dimension_title = self.graph_model.property_titles[self.graph_model.xaxis_id] + ' - ' + \
                          self.graph_model.property_titles[self.graph_model.additional_xaxis_id]
        ret_val = {}
        ret_val[dimension_title] = self.graph_model.filter_unique_vals
        return ret_val

    def get_values_for(self, filter_vals):
        ret_val = {}
        for additional_xaxis, values in self.graph_model.lines_map.iteritems():
            matches = self.find_matches_in(values, filter_vals)
            if matches and len(matches) > 0:
                ret_val[additional_xaxis] = matches
        return ret_val

    def translate_to_json(self, filters):
        chart_data = []
        model_name = self.graph_model.lines_map[self.graph_model.lines_map.keys()[0]][0].model.__class__.__name__
        dimension_idx = self.graph_model.xaxis_id
        model_cls = get_class('platforms_graphs.model.'+model_name)
        time_dim_strategy = None
        if self.graph_model.property_titles[self.graph_model.xaxis_id] == 'Time':
            time_dim_strategy = self.time_as_dimension_strategy if self.time_as_dimension_strategy else time_horizon
        lines_map = {}
        for curr_dim, pvals in self.graph_model.lines_map.items():
            dim = time_dim_strategy(curr_dim) if time_dim_strategy else curr_dim
            if time_dim_strategy:
                for d in dim:
                    if d not in lines_map:
                        lines_map[d] = []
                    for pval in pvals:
                        lines_map[d].append(pval)
            else:
                if dim not in lines_map:
                    lines_map[dim] = []
                for pval in pvals:
                        lines_map[dim].append(pval)
        sorted_lines_map = sorted(lines_map.items(), key=lambda (k,v):model_cls.get_sort_value(dimension_idx, k, time_dim_strategy.__name__)) if time_dim_strategy else sorted(lines_map.items(), key=lambda (k,v):model_cls.get_sort_value(dimension_idx, k))
        for (curr_dimension, plot_vals) in sorted_lines_map:
            matches = self.find_matches_in(plot_vals, filters)
            data_row = {'dimension1':curr_dimension}
            for co_ord in matches:
                key = co_ord[0]
                if self.graph_model.property_titles[self.graph_model.additional_xaxis_id] == 'Time':
                    times = self.time_strategy(key) if self.time_strategy else time_horizon(key)
                    for time in times:
                        data_row[time] = co_ord[1]
                else:
                    data_row[co_ord[0]] = co_ord[1]
            chart_data.append(data_row)
        return chart_data

class BarGraphView(GraphView):
    def get_values_for(self, filter_vals):
        return self.find_matches_in(self.graph_model.plots, filter_vals)

    def translate_to_json(self, filters):
        chart_data = []
        matches = self.find_matches_in(self.graph_model.plots, filters)
        time_dim_strategy = None
        if self.graph_model.property_titles[self.graph_model.xaxis_id] == 'Time':
            time_dim_strategy = self.time_as_dimension_strategy if self.time_as_dimension_strategy else time_horizon
        plot_dict = {}
        for (x, y) in matches:
            dim = time_dim_strategy(x) if time_dim_strategy else x
            if time_dim_strategy:
                for d in dim:
                    if d not in plot_dict:
                        plot_dict[d] = 0.0
                    try:
                        plot_dict[d] += float(y)
                    except ValueError:
                        plot_dict[d] += 0
            else:
                if dim not in plot_dict:
                    plot_dict[dim] = 0.0
                try:
                    plot_dict[dim] += float(y)
                except ValueError:
                    plot_dict[dim] += 0
        for k, v in plot_dict.iteritems():
            curr_dict = {'dimension1' : k, 'All' : v}
            chart_data.append(curr_dict)
        return chart_data


class AggregateBarGraphView(GraphView):
    def translate_to_json(self, filters):
        chart_data = []
        agg_data = self.graph_model.aggregated_data
        time_dim_strategy = None
        if self.graph_model.property_titles[self.graph_model.xaxis_id] == 'Time':
            time_dim_strategy = self.time_as_dimension_strategy if self.time_as_dimension_strategy else time_horizon
        agg_dim_map = {}
        agg_data_strat = {}
        if time_dim_strategy:
            for dimension1, agg_dim_dict in agg_data.iteritems():
                dim = time_dim_strategy(dimension1)
                for d in dim:
                    if not d in agg_data_strat:
                        agg_data_strat[d] = {}
                    for ad, pvals in agg_dim_dict.iteritems():
                        if not ad in agg_data_strat[d]:
                            agg_data_strat[d][ad] = []
                        for pval in pvals:
                            agg_data_strat[d][ad].append(pval)
        else:
            agg_data_strat = agg_data
        for dimension1, agg_dim_dict in agg_data_strat.iteritems():
            agg_map = {}
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                curr_agg = []
                matches = self.find_matches_in(plot_vals, filters)
                for (x, y) in matches:
                    curr_agg.append((x, y))
                agg_map[agg_dim] = curr_agg
            agg_dim_map[dimension1] = agg_map
        processed_data = self.aggregator_strategy(agg_dim_map) if self.aggregator_strategy else average_aggregator(agg_dim_map)
        for dimension1, avg_value in processed_data.iteritems():
            curr_dict = {'dimension1' : dimension1,
                         'All' : avg_value}
            chart_data.append(curr_dict)
        return chart_data