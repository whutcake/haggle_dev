from platforms_graphs.graph_view import average_aggregator, median_aggregator, blind_addition_aggregator

view_to_graphmodel_mapping = {'LineGraphView':'platforms_graphs.graph_model.LineGraphModelBuilder',
                         'BarGraphView':'platforms_graphs.graph_model.BarGraphModelBuilder',
                         'AggregateBarGraphView':'platforms_graphs.graph_model.AggregateBarGraphModelBuilder'}

model_list = {'AvailedDeal' : 'platforms_graphs.model.AvailedDeal',
              'Deal' : 'platforms_graphs.model.Deal',
              'UserScore' : 'platforms_graphs.model.UserScore'}

aggregator_strategy_list = {'Average' : average_aggregator,
                            'Median' : median_aggregator,
                            'Blind Addition' : blind_addition_aggregator}

graphs = {'dollars-spent':
              {'id':'dollars-spent',
                'dimension_ids':'1, 3, 4',
                'filter_ids':'0, 2',
                'model':'Deal',
                'title':'Dollars Spent',
                'graph_model':'LineGraphModelBuilder',
                'graph_view':'LineGraphView'},
          'dollars-cuisine':
              {'id':'dollars-cuisine',
               'dimension_ids':'3, 4',
               'filter_ids':'0, 1, 2',
               'model':'Deal',
               'title':'Dollars Spent Per Cuisine',
               'graph_model':'BarGraphModelBuilder',
               'graph_view':'BarGraphView'},
          'sales-per-head':
              {'id':'sales-per-head',
               'dimension_ids':'3, 4, 6',
               'filter_ids':'0, 1, 2',
               'model':'Deal',
               'title':'Sales Per Head',
               'graph_model':'AggregateBarGraphModelBuilder',
               'graph_view':'AggregateBarGraphView'},
          'aggregate-user-score':
              {'id':'aggregate-user-score',
               'dimension_ids':'7, 6, 1',
               'filter_ids':'4, 8',
               'model':'UserScore',
               'title':'Aggregated User Score',
               'graph_model':'AggregateBarGraphModelBuilder',
               'graph_view':'AggregateBarGraphView'}
        }