<template>
  <div class="hello">
  </div>
</template>




<script>
// import * as d3 from 'd3'
export default {

  name: 'MainVisualization'

}
</script>







<style>
text {
  color: #fff;
}

path.line {
  fill: none;
  stroke: #ecbc3a;
  stroke-width: 3px;
}

.grid line {
  opacity: 0.05;
}
.xA line {
  opacity: 0.5;
}

/*Some fancy animation to draw chart*/
svg .lineChart > path {
  stroke: #ecbc3a;
  stroke-width: 3;
  stroke-dasharray: 4813.713;
  stroke-dashoffset: 4813.713;
  -webkit-animation-name: draw2;
  animation-name: draw2;
  -webkit-animation-duration: 10s;
  animation-duration: 10s;
  -webkit-animation-fill-mode: forwards;
  animation-fill-mode: forwards;
  -webkit-animation-iteration-count: 1;
  animation-iteration-count: 1;
  -webkit-animation-timing-function: linear;
  animation-timing-function: linear;
}

.ani2 svg .lineChart > path {
  stroke: #ecbc3a;
  -webkit-animation-name: draw-2;
  animation-name: draw-2;
}
.ani1 svg .lineChart > path {
  stroke: #ecbc3a;
  -webkit-animation-name: draw;
  animation-name: draw;
}
#Layer_1 {
  width: 100%;
}
@-webkit-keyframes draw {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}
@keyframes draw {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}

@-webkit-keyframes draw-2 {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}

@keyframes draw-2 {
  85% {
  }
  100% {
    stroke-dashoffset: 0;
  }
}
.text {
  display: inline-block;
  font-size: 3vw;
  margin: 0.5vw 0 1.5vw;
}

svg {
  background-color: #f47166;
}
</style>

