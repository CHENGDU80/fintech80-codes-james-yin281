<template>
    <svg :style="{ stroke: color ? color : (trend(data) >= 0 ? '#00ff00' : '#ff0000'), fill: bg_color ? bg_color : (trend(data) >= 0 ? hexToRgb2('#00ff00', 0.06) : hexToRgb2('#ff0000', 0.06)) }" class="sparkline" :width="width" :height="height" :stroke-width="stroke">
        <path class="sparkline--line" :d="shape" fill="none"></path>
        <path class="sparkline--fill" :d="[shape, fillEndPath].join(' ')" stroke="none"></path>
    </svg>
</template>

<script>

function hexToRgb(hex, opacity) {
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return `rgba(${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}, ${opacity})`
}

export default {
    // props: ["data"],
    props: ["data", "color"],
    methods: {
        trend(data) {
            data = Array.from(data)
            var tot = 0;
            for (let step = 0;  step < data.length - 1; step++) {
                tot += data[step + 1] - data[step]
            }
            // console.log(data)
            return tot / (data.length - 1)
        },
        hexToRgb2(hex, opacity) {
            var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
            return `rgba(${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}, ${opacity})`
        }
    },
    data() {
        return {
            stroke: 3,
            width: 256,
            height: 80,
            bg_color: this.bg_color
        };
    },
    mounted() {
        this.bg_color = this.color ? hexToRgb(this.color, 0.06) : this.color;
        // console.log(this.bg_color);
    },
    computed: {
        shape() {
            const stroke = this.stroke;
            const width = this.width;
            const height = this.height - stroke * 2;
            const data = this.data || [];
            const highestPoint = Math.max.apply(null, data) + 1;
            const coordinates = [];
            const totalPoints = this.data.length - 1;
            data.forEach((item, n) => {
                const x = (n / totalPoints) * width + stroke;
                const y = height - (item / highestPoint) * height + stroke;
                coordinates.push({ x, y });
            });
            if (!coordinates[0]) {
                return (
                    "M 0 " +
                    this.stroke +
                    " L 0 " +
                    this.stroke +
                    " L " +
                    this.width +
                    " " +
                    this.stroke
                );
            }
            const path = [];
            coordinates.forEach((point) =>
                path.push(["L", point.x, point.y].join(" "))
            );
            return ["M" + coordinates[0].x, coordinates[0].y, ...path].join(" ");
        },
        fillEndPath() {
            return `V ${this.height} L 4 ${this.height} Z`;
        },
    },
};
</script>

<style>
svg {
    fill: rgba(31, 140, 235, 0.06);
    transition: all 1s ease-in-out;
}

svg path {
    box-sizing: border-box;
}
</style>