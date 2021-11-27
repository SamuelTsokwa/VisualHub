<template>
  <v-container >
    <v-row no-gutters>
      <v-col>
        <v-row>
          <v-select
          :items="dropDownOptions"
          v-model="select"
          v-on:change="firstDropdown"
          outlined
          ></v-select>
        </v-row>
        <div id="polarChart"></div>
        <v-row >
          <div id="messageCard" style="opacity: 0; margin: auto;width: 50%">
            <v-col :justify="center">
            <v-card 
            class="pa-2"
            outlined
            tile
            :opacity="0"
            >
              <strong>Value: <div id="message"></div></strong>
            </v-card>
          </v-col>
          </div>
        </v-row>
      </v-col>
      <v-col>
       
      </v-col>
    </v-row>
  </v-container>
</template>



<script>
import * as d3 from 'd3'
let d3Ez = require("d3-ez");



export default {

  name: 'MainVisualization',
  components: {
  },
  data() {
    return {
      select: "Number",
      subTitle: "Side Effect Number by Age Group",
      numberTitle: "Side Effect Number by Age Group",
      rateTitle: "Side Effect Rate by Age Group",
      dropDownOptions: ['Number','Rate'],
      data1: {"key": "data", "values": [{"key": "12 to 17", "value": 711}, {"key": "18 to 29", "value": 3014}, {"key": "30 to 39", "value": 3927}, {"key": "40 to 49", "value": 4691}, {"key": "50 to 59", "value": 4665}, {"key": "60 to 69", "value": 3779}, {"key": "70 to 79", "value": 2239}, {"key": "80+", "value": 1326}, {"key": "Unknown", "value": 766}]},
      agRate: {"key": "data", "values": [{"key": "12 to 17", "value": 17.07}, {"key": "18 to 29", "value": 31.21}, {"key": "30 to 39", "value": 44.5}, {"key": "40 to 49", "value": 55.51}, {"key": "50 to 59", "value": 50.97}, {"key": "60 to 69", "value": 42.52}, {"key": "70 to 79", "value": 36.64}, {"key": "80+", "value": 38.88}, {"key": "Unknown", "value": "N/A"}]},
      agNumber: {"key": "data", "values": [{"key": "12 to 17", "value": 711}, {"key": "18 to 29", "value": 3014}, {"key": "30 to 39", "value": 3927}, {"key": "40 to 49", "value": 4691}, {"key": "50 to 59", "value": 4665}, {"key": "60 to 69", "value": 3779}, {"key": "70 to 79", "value": 2239}, {"key": "80+", "value": 1326}, {"key": "Unknown", "value": 766}]}
    };
  },

  mounted() {
    this.generateChart1()
  },
  methods: {
      firstDropdown(a){
        
        if (a == "Rate") {
          if (this.data1 != this.agRate) {
            this.subTitle = this.rateTitle
            this.data1 = this.agRate
            
          }
        } else {
          if (this.data1 != this.Number) {
            this.subTitle = this.numberTitle
            this.data1 = this.agNumber
          }
        }
      },
      generateChart1() {
        // var div = d3.select("body").append("div")
        // .attr("class", "tooltip-donut")
        // .style("opacity", 0);

        var colors = d3Ez.default.palette.categorical(1)
        var title = d3Ez.default.component.title().mainText("Covid Side Effect Incidence").subText(this.subTitle);
        var chart = d3Ez.default.chart.polarAreaChart().colors(colors)
        var legend = d3Ez.default.component.legend().title("Age Groups");

        var myChart = d3Ez.default.base()
        .width(750)
        .height(400)
        .chart(chart)
        .legend(legend)
        .title(title)
        .on('customValueMouseOver', function (d) {
          // div.transition()
          // .duration(50)
          // .style("opacity", 1);

          // div.html(d.value)
          // .style("left", (d3.event.pageX + 10) + "px")
          // .style("top", (d3.event.pageY - 15) + "px");
          d3.select("#message").text(d.value);
          d3.select("#messageCard")
            .transition()
            .duration(50)
            .style("opacity", 1);
        })
        .on('customSeriesMouseOut', function () {
          // div.transition()
          //      .duration('50')
          //      .style("opacity", 0);
          d3.select("#message").text("");
          d3.select("#messageCard")
            .transition()
            .duration(50)
            .style("opacity", 0);
        })

        
        


        d3.select("#polarChart")
        .selectAll('*').remove();

        d3.select("#polarChart")
        .datum(this.data1)
        .call(myChart);
      }
  },
  watch: {
    data1: {
      deep: true,
      handler() { this.generateChart1(); }
    }
},
   
}
</script>







<style>

#creditTag {
  display: none
}




</style>

