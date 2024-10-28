<template>
    <div id="size_element" class="card" style="margin-inline: 5px;">
        <div class="card-body">
            <h4 class="card-title">{{ title }}</h4>
            <p class="card-subtitle mb-4">{{ description }}</p>
            <slot></slot>
        </div>
    </div>
</template>
<script>
export default {
    name : 'CardVue',
    props : {
        title : String,
        description : String
    },
};
</script>
<style>
@import "../assets/css/bootstrap.min.module.css";
@import "../assets/css/icons.min.module.css";
@import "../assets/css/theme.min.module.css";
</style>