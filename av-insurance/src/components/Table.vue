<template>
    <div class="table-responsive">
        <table class="table table-centered table-striped table-nowrap">
            <thead>
                <tr>
                    <th v-for="(item, index) in labels" :key="index">{{ item.name }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(user_data, index) in data">
                    <td @click="() => this.$emit('clicked', index)" v-for="(feature, feature_index) in user_data">
                        <div :style="{backgroundColor: labels[feature_index].data.labels.filter(a => a.name == feature)[0].color, width: 'fit-content', paddingInline: '5px', borderRadius: '5px', color: 'white' }" v-if="labels[feature_index].type == 'label'">
                            {{ feature }}
                        </div>
                        <div v-else>
                            {{ feature }}
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    
</template>
<script>

// console.log(labels[4].data.labels.filter(a => a.name == "Expired")[0].color)

export default {
    props: {
        data: Array,
        labels: Array,
        onclick: () => {}
    }
}
</script>
<style>
@import "../assets/css/bootstrap.min.module.css";
@import "../assets/css/icons.min.module.css";
@import "../assets/css/theme.min.module.css";
</style>