def gauge(value):
    gaugeData = [{
        "value": 0,
        "name": 'Match %',
        "detail": {
        "valueAnimation": True,
        "offsetCenter": ['0%', '0%']
            }
        }]
    option = {
    "series": [
        {
        "type": "gauge",
        "startAngle": 90,
        "endAngle": -270,
        "pointer": {
            "show": False,
        },
        "progress": {
            "show": True,
            "overlap": False,
            "roundCap":False,
            "clip": False,
            "backgroundColor": '#11D1F9',
            "itemStyle": {
            "color": '#E96605', 
            "borderWidth": 0,
            "borderColor": "light blue"
            }
        },
        "axisLine": {
            "lineStyle": {
            "width": 40
            }
        },
        "splitLine": {
            "show": False,
            "distance": 0,
            "length": 20
        },
        "axisTick": {
            "show": False
        },
        "axisLabel": {
            "show": False,
            "distance": 50
        },
        "data": gaugeData,
        "detail": {
            "valueAnimation": True,
            "offsetCenter": ['0%', '0%'],
            "width": 40,
            "height": 14,
            "fontSize": 24,
            "color": 'inherit',
            "borderColor": 'inherit',
            "borderRadius": 0,
            "borderWidth": 0,
            "formatter": '{value}%'
        },
        }
    ]
    }
    return gaugeData ,option