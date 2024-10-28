<template>
    <div class="card" style="margin-inline: 5px;">
        <div class="card-body">
            <div class="row align-items-center">
                <div class="col">
                    <h6 class="text-uppercase font-size-12 text-muted mb-3">{{ title }}</h6>
                    <span class="h3 mb-0"> {{ suffix }} {{ format(+price) }} </span>
                </div>
                <div class="col-auto">
                    <span v-if="pourcentage" class="badge badge-soft-success">{{ pourcentage }}</span>
                </div>
            </div>

            <slot></slot>
            <!-- <div id="sparkline1" class="mt-3"></div> -->

        </div>
    </div>
</template>
<script>

export default {
    props: {
        title: String,
        price: String,
        pourcentage: String,
        suffix : String
    },
    methods: {
        format(num, fix) {
            var p = num.toFixed(fix).split(".");
            return p[0].split("").reduceRight(function (acc, num, i, orig) {
                if ("-" === num && 0 === i) {
                    return num + acc;
                }
                var pos = orig.length - i - 1
                return num + (pos && !(pos % 3) ? "," : "") + acc;
            }, "") + (p[1] ? "." + p[1] : "");
        }
    }
}

// const {title, pourcentage, price} = defineProps(['title', 'price', 'pourcentage'])
</script>
<style>
@import "../assets/css/bootstrap.min.module.css";
@import "../assets/css/icons.min.module.css";
@import "../assets/css/theme.min.module.css";

.lil_margin {
    margin: 10px
}
</style>