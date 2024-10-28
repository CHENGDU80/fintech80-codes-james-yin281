<template>
    <div style="display:flex; flex-wrap: wrap; justify-content: center;">
    </div>
    <div style="display:flex; justify-content: center;">
        <Card
            title="Claim amount"
            description="A distribution of the claim amounts"
        >
            <Histogram
                :data="[5,]"
            >
            </Histogram>
        </Card>
        <!-- <Heatmap :countyOccurrences="sampleCountyOccurrences" /> -->
    </div>
</template>
<script>
import Histogram from '@/components/Histogram.vue'
import Card from '@/components/Card.vue'

export default {
    components: { Histogram, Card },
    // data() {
    //     return {
    //         sampleCountyOccurrences: [
    //           "05000US01001", "05000US01001", "05000US01003", "05000US01003",
    //           "05000US01003", "05000US01005", "05000US01007", "05000US01009"
    //         ]
    //     }
    // }
}
</script>