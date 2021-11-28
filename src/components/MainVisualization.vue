<template>
  <v-container >
    <v-row no-gutters>
      <v-col>
        <v-row>
          <v-select
          :items="dropDownOptions"
          v-model="select"
          v-on:change="firstDropdown"
          dense
          outlined
          ></v-select>
        </v-row>
        <div id="polarChart"></div>
      </v-col>
      <v-col>
        <v-row>
            <v-select
            :items="dropDownOptions2"
            v-model="select2"
            v-on:change="secondDropdown"
            dense
            outlined
            ></v-select>
          </v-row>
          <div id="radarChart"></div>
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
      select2: "Number",
      subTitle: "Side Effect Number by Age Group",
      subTitle1: "Side Effect Number by Age Group and sex",
      numberTitle: "Side Effect Number by Age Group",
      rateTitle: "Side Effect Rate by Age Group",
      numberTitle1: "Side Effect Number by Age Group and sex",
      rateTitle1: "Side Effect Rate by Age Group and sex",
      dropDownOptions: ['Number','Rate'],
      dropDownOptions2: ['Number','Rate'],
      data1: {"key": "data1", "values": [{"key": "12 to 17", "value": 711}, {"key": "18 to 29", "value": 3014}, {"key": "30 to 39", "value": 3927}, {"key": "40 to 49", "value": 4691}, {"key": "50 to 59", "value": 4665}, {"key": "60 to 69", "value": 3779}, {"key": "70 to 79", "value": 2239}, {"key": "80+", "value": 1326}, {"key": "Unknown", "value": 766}]},
      agRate: {"key": "data2", "values": [{"key": "12 to 17", "value": 17.07}, {"key": "18 to 29", "value": 31.21}, {"key": "30 to 39", "value": 44.5}, {"key": "40 to 49", "value": 55.51}, {"key": "50 to 59", "value": 50.97}, {"key": "60 to 69", "value": 42.52}, {"key": "70 to 79", "value": 36.64}, {"key": "80+", "value": 38.88}, {"key": "Unknown", "value": "N/A"}]},
      agNumber: {"key": "data1", "values": [{"key": "12 to 17", "value": 711}, {"key": "18 to 29", "value": 3014}, {"key": "30 to 39", "value": 3927}, {"key": "40 to 49", "value": 4691}, {"key": "50 to 59", "value": 4665}, {"key": "60 to 69", "value": 3779}, {"key": "70 to 79", "value": 2239}, {"key": "80+", "value": 1326}, {"key": "Unknown", "value": 766}]},
      data2: [{"key": "Male", "values": [{"key": "12 to 17", "value": 415}, {"key": "18 to 29", "value": 1006}, {"key": "30 to 39", "value": 857}, {"key": "40 to 49", "value": 893}, {"key": "50 to 59", "value": 992}, {"key": "60 to 69", "value": 976}, {"key": "70 to 79", "value": 644}, {"key": "80+", "value": 321}, {"key": "Unknown", "value": 147}]}, {"key": "Female", "values": [{"key": "12 to 17", "value": 331}, {"key": "18 to 29", "value": 1949}, {"key": "30 to 39", "value": 2991}, {"key": "40 to 49", "value": 3699}, {"key": "50 to 59", "value": 3576}, {"key": "60 to 69", "value": 2698}, {"key": "70 to 79", "value": 1537}, {"key": "80+", "value": 975}, {"key": "Unknown", "value": 362}]}],
      agMFRate: [{"key": "Male", "values": [{"key": "12 to 17", "value": 19.66}, {"key": "18 to 29", "value": 20.7}, {"key": "30 to 39", "value": 19.68}, {"key": "40 to 49", "value": 21.67}, {"key": "50 to 59", "value": 22.13}, {"key": "60 to 69", "value": 22.63}, {"key": "70 to 79", "value": 22.22}, {"key": "80+", "value": 23.5}, {"key": "Unknown", "value": 0}]}, {"key": "Female", "values": [{"key": "12 to 17", "value": 16.15}, {"key": "18 to 29", "value": 40.86}, {"key": "30 to 39", "value": 67.09}, {"key": "40 to 49", "value": 85.59}, {"key": "50 to 59", "value": 76.68}, {"key": "60 to 69", "value": 59.04}, {"key": "70 to 79", "value": 47.89}, {"key": "80+", "value": 47.86}, {"key": "Unknown", "value": 0}]}],
      agMFNumber: [{"key": "Male", "values": [{"key": "12 to 17", "value": 415}, {"key": "18 to 29", "value": 1006}, {"key": "30 to 39", "value": 857}, {"key": "40 to 49", "value": 893}, {"key": "50 to 59", "value": 992}, {"key": "60 to 69", "value": 976}, {"key": "70 to 79", "value": 644}, {"key": "80+", "value": 321}, {"key": "Unknown", "value": 147}]}, {"key": "Female", "values": [{"key": "12 to 17", "value": 331}, {"key": "18 to 29", "value": 1949}, {"key": "30 to 39", "value": 2991}, {"key": "40 to 49", "value": 3699}, {"key": "50 to 59", "value": 3576}, {"key": "60 to 69", "value": 2698}, {"key": "70 to 79", "value": 1537}, {"key": "80+", "value": 975}, {"key": "Unknown", "value": 362}]}],
      
    };
  },

  mounted() {
    this.generateChart1()
    this.generateChart2()
  },
  methods: {
      secondDropdown(a) {
        if (a == "Rate") {
          if (this.data2 != this.agMFRate) {
            this.subTitle1 = this.rateTitle1
            this.data2 = this.agMFRate
            
          }
        } else {
          if (this.data2 != this.agMFNumber) {
            this.subTitle1 = this.numberTitle1
            this.data2 = this.agMFNumber
          }
        }
      },
      firstDropdown(a){
        
        if (a == "Rate") {
          if (this.data1 != this.agRate) {
            this.subTitle = this.rateTitle
            this.data1 = this.agRate
            
          }
        } else {
          if (this.data1 != this.agNumber) {
            this.subTitle = this.numberTitle
            this.data1 = this.agNumber
          }
        }
      }
      ,
      generateChart1() {
        var div = d3.select("body").append("div")
        .attr("class", "tooltip-donut")
        .style("opacity", 0);

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
        .on('customValueMouseOver', (event,d) =>{ 
          div.transition()
          .duration(50)
          .style("opacity", 1);
          div.html(this.data1 == this.agRate ? d.value + "%": d.value)
          .style("left", (event.pageX + 10) + "px")
          .style("top", (event.pageY - 15) + "px");
        })
        .on('customValueMouseOut', function () {
          div.transition()
               .duration('50')
               .style("opacity", 0);
        })



        d3.select("#polarChart")
        .selectAll('*').remove();

        d3.select("#polarChart")
        .datum(this.data1)
        .call(myChart);
      },
      generateChart2() {
        

        var colors = d3Ez.default.palette.categorical(1)
        var title = d3Ez.default.component.title().mainText("Covid Side Effect Incidence").subText(this.subTitle1);
        var chart = d3Ez.default.chart.radarChart().colors(colors)
        var legend = d3Ez.default.component.legend().title("Sex");

        var myChart = d3Ez.default.base()
        .width(750)
        .height(400)
        .chart(chart)
        .legend(legend)
        .title(title)




        d3.select("#radarChart")
        .selectAll('*').remove();

        d3.select("#radarChart")
        .datum(this.data2)
        .call(myChart);
      }
  },
  watch: {
    data1: {
      deep: true,
      handler() { this.generateChart1(); }
    },
    data2: {
      deep: true,
      handler() { this.generateChart2(); }
    }
},
   
}
</script>







<style>

div.tooltip-donut {
     position: absolute;
     text-align: center;
     padding: .5rem;
     background: #FFFFFF;
     color: #313639;
     border: 1px solid #313639;
     border-radius: 8px;
     pointer-events: none;
     font-size: 1.3rem;
}

#creditTag {
  display: none
}




</style>

