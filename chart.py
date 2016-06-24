
import uuid

RESET_OPTION = """
                require(%s,function(echarts){
                var myChart = echarts.init(document.getElementById('%s'),'%s');
                myChart.setOption(%s);
                });
                """
APPEND_ELEMENT = """
$('#{id}').attr('id','{id}'+'_old');
element.append('<div id="{id}" style="width: 600px;height:400px;"></div>');"""

OPTION_TEMPLATE = {
        'title': {
            'text': ''
        },
        'tooltip': {'axisPointer':{'type':''}},
        'legend': {
            'data':[]
        },
        'xAxis': {
            'data': []
        },
        'yAxis': {},
        'series': []
    }

class Chart():
    def __init__(self,**kwargs):
        self._chartId = str(uuid.uuid4())
        self._option = deepcopy(OPTION_TEMPLATE)    
        self._kwargs_chart_ = kwargs
        self._theme = ''
        

    def set_legend(self,):
        pass
    
    
    def set_theme(self,theme):
        """Set the theme of the chart.
        theme: {'dark','vintage','rima','shine','infographic','dark'}, default None
        """
        self._theme = theme
        return self
        
    
    
    def resync_data(self,data):
        """Update data but still using the same chart option.
        Currently just update the current cell it exist, but not the chart option
        itself.
        
        Parameters
        ----------
        data: pd.DataFrame
         
        """
        option = make_chart(data,**self._kwargs_chart_)._option
        return Javascript(self._get_resync_option_strings(option))
    
    def replot(self,chart):
        """Replot entire chart to its current cell"""
        return Javascript(self._get_resync_option_strings(chart._option))
    
    def _get_resync_option_strings(self,option):
        """Resync Chart option"""
        
        return RESET_OPTION % (list(d_paths.keys()).__repr__(),
                               self._chartId,
                               self._theme,
                               json.dumps(option))
    
    
    def set_tooltip(self,trigger='axis',axis_pointer='shadow'):
        """Set Tooltip options.
        
        Parameters
        ----------
        trigger: {'axis',None}, default 'axis'
            When tooltip should be triggered. Default to axis
        axis_pointer: {'shadow',None}, default 'shadow'
            Effect of pointing the axis.
        
        
        Returns
        -------
        
        """
        
        self._option['tooltip']['trigger'] = trigger
        self._option['tooltip']['axisPointer']['type'] = axis_pointer
        return self
    
    
    def get_option(self):
        global optionx
        return option
    
    
    def set_title(self,title):
        """Set title for the plot"""
        self._option['title']['text'] = title
        return self
    
    
    def flip_axes(self):
        """Flip the axes to make it horizontal"""
        self._axes_swapped = not self._axes_swapped
        self._option['xAxis'],self._option['yAxis'] = self._option['yAxis'],self._option['xAxis']
        return self
    
    
    def _repr_javascript_(self):
        """Embedding the result of the plot to Jupyter"""
        return (APPEND_ELEMENT.format(id=self._chartId))+\
                (self._get_resync_option_strings(self._option))
        
    _axes_swapped = True
    _kwargs_chart_ = {}
        
        #return RESET_OPTION % (self._chartId,json.dumps(option))
    
    