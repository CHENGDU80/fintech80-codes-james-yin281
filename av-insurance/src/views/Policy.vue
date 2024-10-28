<template>
    <Card
        style="width:100%"
        title="Policy table"
        description="A list of all the policy associated to the user"
    >
        <Table
            @clicked="(feature_index) => this.$router.push(`/policy/${feature_index}`)"
            :data="data"
            :labels="labels"
        ></Table>
    </Card>
</template>
<script>
import Card from '@/components/Card.vue';
import Table from '@/components/Table.vue';

var labels =
    [
        {
            name: "Client",
            data: {},
            type: "text"
        },
        {
            name: "Location",
            data: {},
            type: "text"
        },
        {
            name: "Car Usage",
            data: {},
            type: "text"
        },
        {
            name: "Price",
            data: {},
            type: "text"
        },
        {
            name: "Insurance Status",
            data: {
                labels: [
                    {
                        name: "Expired",
                        color: "#ff0000"
                    },
                    {
                        name: "Expiring in 7 Days",
                        color: "#ffc500"
                    },
                    {
                        name: "Active",
                        color: "#00ee00"
                    }
                ]
            },
            type: "label"
        }
    ]

var data = [
    ["Xi Dao", "Beijing", "845.6", "64798", "Expired"],
    ["Zhao an", "Shanghai", "815.6", "64798", "Active"],
    ["Wang Zhao", "Chengdu", "845.6", "64798", "Expiring in 7 Days"]
]

export default {
    components: { Table, Card },
    data () {
        return {
            data: data,
            labels: labels
        }
    }
}
</script>