ENV_NAME="haggle-test1.appspot.com"
TEMPLATE_VALUES = {
        'discount_trends': {
            'header': 'Discount Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns average maximum and minimum discounts being offered in the given area.',
            'endpoint': 'aggregate_campaigns',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                },
            'response':{
                    'average_max_discount': 'The average maximum discount being offered in a specified area',
                    'average_min_discount': 'The average minimum discount being offered in a specified area'
                }
            },
        'score_preference_trends': {
            'header': 'Score Preference Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns trends in user profile preferences restaurants have in a given area',
            'endpoint': 'aggregate_campaigns',
            'params': {
                'property': { 
                    'value': 'score_preference_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters)'
                    }
                },
            'response': {
                    'High History': "Number of restaurants which prefer users who have a history of eating the restaurant's own cuisine",
                    'High Loyalty': 'Number of restaurants which prefer users who frequent their place',
                    'Social Influence': 'Number of restaurants which prefer social influencers',
                    'High Roller': 'Number of restaurants which prefer users with high bank roll'
                }
            },
        'bids_trends': {
            'header': 'Bids Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': "Returns Users' bidding trends in the given area.",
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'bids_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters)'
                    }
                },
            'response': {
                    'got close':'Number of users who got a final offer quite close to what they bid for',
                    'got what they wanted':'Number of users who were offered what they bid for',
                    'way off': 'Number of users who got an offer much less than what they bid for'
                }
            },
        'user_trends': {
            'header': 'User Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Trends in profiles of all users who are Haggling via the Haggle platform',
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'user_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                },
            'response': {
                    'High Loyalty': 'The number of users who were offered a discount because of their high loyalty',
                    'High History': 'The number of users who were offered a discount because of their high history',
                    'Social Butterfly': 'The number of users who were offered a discount because of their high influence',
                    'High Roller': 'The number of users who were offered a discount because of their high purchasing power'
                }
            },
        'time_trends': {
            'header': 'Time Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description':'Discover what times an area goes deal crazy. Time Trends helps you plan for all the Haggle Happy Hours in your area. Or, look up time trends in other areas to see how your neighborhood shores up against them.',
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'time_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                },
            'response': {
                    'late_dinner':'Number of people who visited in the late hours',
                    'brunch': 'Number of people who visited for brunch',
                    'lunch': 'Number of people who visited for dinner',
                    'breakfast': 'Number of people who visited for breakfast',
                    'dinner': 'Number of people who visited for dinner'
                }
            },
        'average_spending': {
            'header': 'Average Spending',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Are you attracting big spenders or mass selling those hot cakes? Whatever your strategy is, check out if you are above or below the competition in your area.',
            'endpoint': 'aggregate_deals',
            'params': {
                'property': { 
                    'value': 'average_spending',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                },
            'response': {
                    'average_spend_dollars':'Average amount spent in the area specified',
                }
            },
            'users_search': {
            'header': 'Users Search',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns a list of users that match your query. If you are a restaurant, check out our <a href="/endpoints/render?property=vendors_deal_history">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'uid': {
                    'value': 21325632,
                    'description': "A specific user's ID"
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'users_history': {
            'header': 'Users History',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum history score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'min': {
                    'value': 1,
                    'description': 'Minimum History score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum History score.'
                    },
                }
            },
            'users_loyalty': {
            'header': 'Users Loyalty',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum loyalty score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                 'min': {
                    'value': 1,
                    'description': 'Minimum Loyalty score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum Loyalty score.'
                    },
                }
            },
            'users_social_influence': {
            'header': 'Users Social Influence',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum Social Influence score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                 'min': {
                    'value': 1,
                    'description': 'Minimum Social Influence score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum Social Influence score.'
                    },
                }
            },
            'users_purchasing_power': {
            'header': 'Users Purchasing Power',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': '(Vendors only) Returns a list of customers with the specified minimum/maximum purchasing power score. If no parameters are set, returns a sorted list of previous customers. <br>Check out our <a href="http://google.com">Vendor deals history</a> search function to analyze your previous customers.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                 'min': {
                    'value': 1,
                    'description': 'Minimum Purchasing Power score.'
                    },
                'max': {
                    'value': 4,
                    'description': 'Maximum Purchasing Power score.'
                    },
                }
            },
            'vendors_categories': {
            'header': 'Vendors Categories',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns either the entire tree or leaf of our categories tree.',
            'endpoint': 'categories',
            'params': {
                'property': { 
                    'value': 'categories',
                    'description': 'property_desc'
                    },
                'leaf': {
                    'value': 'American',
                    'description': '(Optional) Node which you want to start with. Leave blank for the whole tree.'
                    },
                }
            },
            'users_deals': {
            'header': 'Vendors Deal History',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Analyze your data. Grab your business by the horns. <br>Returns a list of deals based on your parameters.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'since': {
                    'value': 20130320,
                    'description': 'Since (optional) (YYYYMMDD)'
                    },
                'before': {
                    'value': 20130326,
                    'description': 'Before (optional) (YYYYMMDD)'
                    },
                },
            'other_params': '''Other (optional) parameters: <br><table class="table table-hover">
                    <tr>
                        <th>Variable</th>
                        <th>Description</th>
                        <th>HTML param</th>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum Purchasing Power</td>
                        <td>Filters deals by the Purchasing Power of the customers</td>
                        <td>minpp, maxpp</td>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum Loyalty</td>
                        <td>Filters deals by the Loyaly of the customers</td>
                        <td>minlty, maxlty</td>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum Social Influence</td>
                        <td>Filters deals by the Social Influence of the customers</td>
                        <td>minsoc, maxsoc</td>
                    </tr>
                    <tr>
                        <td>Minimum/Maximum History</td>
                        <td>Filters deals by the History of the customers</td>
                        <td>minhist, maxhist</td>
                    </tr>
                </table>''',
            },
            'vendors_explore': {
            'header': 'Vendors Explore',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns our REST API output for finding nearby vendors.',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude of your search point'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'vendors_search': {
            'header': 'Vendors Search',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns vendors that match your parameters. See our <a href="/endpoints/render?property=vendors_explore">Explore API</a> if you want our REST API vendor search.',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'WAIT WHAT VARIABLES DO I PUT IN.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'vendors_campaigns': {
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'header': 'Vendors Campaigns',
            'description': 'Returns a list of active campaigns based on your search query. See also our VENDORS EXPLORE api call for finding nearby campaigns.',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters)'
                    },
                'time_start': { 
                    'value': 1230,
                    'description': 'Time in HHMM format of campaign start time'
                    },
                'time_end': { 
                    'value': 2359,
                    'description': 'Time in HHMM format of campaign end time'
                    },
                }
            },
            'vendors_hours': {
            'header': 'Vendors Hours',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            #TOFIX
            'description': 'Returns analytic hours of campaigns? I do not remember why we thought this was a good api endpoint.',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'WAIT WHAT VARIABLES DO I PUT IN.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'vendors_tips': {
            'header': 'Vendors Explore',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            #TOFIX
            'description': 'Returns tips about a given restaurant ID? Do we even have an implementation for tips?',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'WAIT WHAT VARIABLES DO I PUT IN.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'vendors_user_trends': {
            'header': 'Vendors User Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Lets you understand trends in the profiles of users who are visiting your restaurant',
            'endpoint': 'vendors_campaigns',
            'params': {
                'property': { 
                    'value': 'vendors_user_trends',
                    'description': 'property_desc'
                    },
                'vendor_id': {
                    'value': 5692188943974400,
                    'description': 'Vendor ID'
                    },
                },
            'response':{
                'High Loyalty': 'The number of users who were offered a discount because of their loyalty towards you',
                'High History': 'The number of users who were offered a discount because of their history of liking your cuisine',
                'Social Butterfly': 'The number of users who were offered a discount because of their influence in your neighborhood',
                'High Roller': 'The number of users who were offered a discount because of their high purchasing power',
            }
            },
            'vendors_time_trends': {
            'header': 'Vendors Time Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Find trends in the times users have been visiting your restaurant',
            'endpoint': 'vendors_campaigns',
            'params': {
                'property': { 
                    'value': 'vendors_time_trends',
                    'description': 'property_desc'
                    },
                'vendor_id': {
                    'value': 5692188943974400,
                    'description': 'Vendor ID'
                    },
                },
            'response': {
                    'late_dinner':'Number of people who visited in the late hours',
                    'brunch': 'Number of people who visited for brunch',
                    'lunch': 'Number of people who visited for dinner',
                    'breakfast': 'Number of people who visited for breakfast',
                    'dinner': 'Number of people who visited for dinner'
                }
            },
            'vendors_average_spending': {
            'header': 'Vendors Average Spending',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Find out the average amount people are spending in your restaurant',
            'endpoint': 'vendors_campaigns',
            'params': {
                'property': { 
                    'value': 'vendors_average_spending',
                    'description': 'property_desc'
                    },
                'vendor_id': {
                    'value': 5692188943974400,
                    'description': 'Vendor ID'
                    },
                },
            'response': {
                    'average_spend_dollars': 'Average amount spent in your restaurant'
                }
            },
            'vendors_current_deals': {
            'header': 'Vendors Current Deals',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns a list of users who have pending deals with your store',
            'endpoint': 'vendors_deals',
            'params': {
                'property': { 
                    'value': 'vendors_current_deals',
                    'description': 'property_desc'
                    },
                'vendor_id': {
                    'value': 5692188943974400,
                    'description': 'Vendor ID'
                    },
                },
            'response': {
                    'bargains': "A list of all the current bargains which still haven't been claimed",
                    'count': "A count of the current bargains which still haven't been claimed"
                }
            },
            'vendors_links': {
            'header': 'Vendors Links',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns analytical data of your business and its customers. You can give permissions to which apps access this data at /vendor_admin_permissions_edit',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'WAIT WHAT VARIABLES DO I PUT IN.'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude of the location.'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'vendors_accept_deal': {
            'header': 'Vendors Accept Deal',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to accept an offer made by a customer. You can give permissions to which apps can make this post for you at /vendor_admin_permissions_edit',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'uID': {
                    'value': 40.745619,
                    'description': 'User ID'
                    },
                'dID': {
                    'value': -73.985296,
                    'description': 'Deal ID'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'vendors_request_deal': {
            'header': 'Vendors Request Deal',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to request a deal to a vendor. I think.',
            'endpoint': 'vendors_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'uID': {
                    'value': 40.745619,
                    'description': 'User ID'
                    },
                'dID': {
                    'value': -73.985296,
                    'description': 'Deal ID'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'aggregate_campaigns_hours_trends': {
            'header': 'Campaign Hours Trends',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to request a deal to a vendor. I think.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'individual_campaigns_search': {
            'header': 'Vendors Request Deal',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to request a deal to a vendor. I think.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'individual_campaigns_hours': {
            'header': 'Individual Campaign Hours',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns individual campaign hours.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'individual_campaigns_score_preferences': {
            'header': 'Individual Campaign Score Preferences',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns individual campaign score preferences.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'individual_campaigns_max_discount': {
            'header': 'Individual Campaign Maximum Discount',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns individual campaign maximum discount.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'individual_campaigns_minimum_discount': {
            'header': 'Individual Campaign Minimum Discount',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns individual campaign minimum discount.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'lat': {
                    'value': 40.745619,
                    'description': 'Latitude'
                    },
                'lon': {
                    'value': -73.985296,
                    'description': 'Longitude'
                    },
                'radius': { 
                    'value': 3000,
                    'description': 'Radius (in meters).'
                    }
                }
            },
            'individual_campaigns_delete': {
            'header': 'Delete Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to delete a campaign.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Campaign ID.'
                    }
                }
            },
            'individual_campaigns_end': {
            'header': 'End Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to delete a campaign.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Campaign ID.'
                    }
                }
            },
            'individual_campaigns_start': {
            'header': 'Start Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to start a campaign.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Campaign ID.'
                    }
                }
            },
            'individual_deals_search': {
            'header': 'Search Deals',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns information about your deals.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_delete': {
            'header': 'Start Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to delete a deal.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_user_id': {
            'header': 'UID of Deals',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns information about your deals.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_bid': {
            'header': 'Bids Deals?',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns information about your deals.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_offer': {
            'header': 'Offers Deals?',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'Returns information about your deals.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_delete': {
            'header': 'Start Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to delete a deal.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_delete': {
            'header': 'Start Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to delete a deal.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_delete': {
            'header': 'Start Campaign',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to delete a deal.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_make_public': {
            'header': 'Make Public',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to make a deal public.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'individual_deals_make_private': {
            'header': 'Make Private',
            'url': 'https://'+ENV_NAME+'/api/analytics/',
            'description': 'POST method to make a deal priate.',
            'endpoint': 'users_search',
            'params': {
                'property': { 
                    'value': 'discount_trends',
                    'description': 'property_desc'
                    },
                'id': { 
                    'value': 34523323,
                    'description': 'Deal ID.'
                    }
                }
            },
            'vendors_general_overview': {
            'header': 'Overview',
            'url': 'local',
            'description': 'Returns an overview of the harmonized restaurants in our datastore',
            'endpoint': '/api/restaurants_overview',
            'params': {},
            'response':{
                'cuisine': 'A unique set of all the cuisines our harmonized restaurants belong to',
                'neigh': 'A unique set of all the neighborhoods our harmonized restaurants belong to',
                'rest_count': 'The total number of harmonized restaurants in our datastore'
            }
            },
            'vendors_general_explore': {
            'header': 'Explore',
            'url': 'local',
            'description': 'Returns harmonized restaurants from our datastore which match your search criteria',
            'endpoint': '/api/restaurants',
            'params': {
                    'dlr_rating': {
                        'value': '',
                        'description': 'Dollar Rating'
                        },
                    'lat': {
                        'value': '',
                        'description': 'Latitude'
                        },
                    'lon': {
                        'value': '',
                        'description': 'Longitude'
                        },
                    'radius': {
                        'value': '',
                        'description': 'Radius (in meters).'
                        },
                    'cuisine': {
                        'value': '',
                        'description': 'Cuisine'
                        },
                    'name': {
                        'value': '',
                        'description': 'Restaurant name'
                        },
                    'neigh': {
                        'value': '',
                        'description': 'Neighborhood'
                        }
                },
            'response': {
                    'count': 'Total number of restaurants which match your search query',
                    'matches': 'List of all the restaurants which match you search query'

                }
            }
        }

client_id = 'MQ2SDSAN0EVC11ZX0QV6O411GQJZP2KZ1T10L'
client_secret = 'WJXHM3SAPVMTGBDV2SHMBS5J54NGLPDA5444G'
redirect_uri = 'http://haggle-dev.appspot.com/api/test'
