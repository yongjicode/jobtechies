<template>
    <div>
        <Head>
            <Title>Vue Textarea Component</Title>
            <Meta name="description" content="Textarea adds styling, key filtering and autoResize functionality to standard textarea element." />
        </Head>

        <div class="content-section introduction">
            <div class="feature-intro">
                <h1>Textarea</h1>
                <p>Textarea is a multi-line text input element.</p>
            </div>
            <AppDemoActions />
        </div>

        <div class="content-section implementation">
            <div class="card">
                <h5>Basic</h5>
                <Textarea v-model="value1" rows="5" cols="30" />

                <h5>Auto Resize</h5>
                <Textarea v-model="value2" :autoResize="true" rows="5" cols="30" />

                <h5>Disabled</h5>
                <Textarea v-model="value3" disabled rows="5" cols="30" />
            </div>
        </div>

        <TextareaDoc />
    </div>
</template>

<script>
import TextareaDoc from './TextareaDoc';

export default {
    data() {
        return {
            value1: '',
            value2: '',
            value3: ''
        };
    },
    components: {
        TextareaDoc: TextareaDoc
    }
};
</script>
