<template>
    <div>
        <Head>
            <Title>Job Explorer</Title>
            <Meta name="description" content="Public Assessible One-stop Job Searching Engine" />
        </Head>

        <div class="content-section introduction">
            <div class="feature-intro">
                <h1>Job Explorer</h1>
                <p>Your One-Stop Job Searching Engine</p>
            </div>
            <AppDemoActions />
        </div>

        <div class="content-section implementation">
            <div class="card">
                <!--
                <h5>Table Integration</h5>
                <p>A custom equals filter that checks for exact case sensitive value is registered and defined as a match mode of a column filter.</p>
                -->
                <DataTable v-model:filters="filters" :value="customers" :paginator="true" :rows="10" responsiveLayout="scroll" dataKey="id" filterDisplay="row" >
                    
                    <Column sortable header="Track" filterField="Track" :filterMatchModeOptions="matchModeOptions">
                        <template #body="{ data }">
                            <span class="image-text">{{ data.Track }}</span>
                        </template>
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by Track - ${filterModel.matchMode}`" />
                        </template>
                    </Column>
                    <Column header="SubTrack" filterField="SubTrack" :filterMatchModeOptions="matchModeOptions">
                        <template #body="{ data }">
                             <span class="image-text">{{ data.SubTrack }}</span>
                        </template>
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by SubTrack - ${filterModel.matchMode}`" />
                        </template>
                    </Column>
                    <Column header="Role" filterField="Role" :filterMatchModeOptions="matchModeOptions">
                        <template #body="{ data }">
                            <span class="image-text">{{ data.Role }}</span>
                        </template>
                        <template #filter="{ filterModel, filterCallback }">
                            <InputText v-model="filterModel.value" type="text" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by Role - ${filterModel.matchMode}`" />
                        </template>
                    </Column>

                    
                    <Column headerStyle="min-width: 3rem; text-align: center" bodyStyle="text-align: center; overflow: visible">
                        <template #body>
                            <Button type="button" icon="pi pi-cog"></Button>
                        </template>
                    </Column>
                </DataTable>
            </div>
        </div>

        <FilterServiceDoc />
    </div>
</template>

<script>
import { FilterMatchMode, FilterService } from 'primevue/api';
import CustomerService from '../../service/CustomerService';
import FilterServiceDoc from './FilterServiceDoc';
const YOUR_FILTER = 'YOUR FILTER';


export default {
    data() {
        return {
            customers: null,
            filters: {
                'Track': { value: null, matchMode: FilterMatchMode.STARTS_WITH  },
                'SubTrack': { value: null, matchMode: FilterMatchMode.STARTS_WITH },
                'Role': { value: null, matchMode: FilterMatchMode.STARTS_WITH }
            },
            matchModeOptions: [
                { label: 'Your Equals', value: YOUR_FILTER },
                { label: 'Starts With', value: FilterMatchMode.STARTS_WITH }
            ],
            loading: true
        };
    },
    created() {
        this.customerService = new CustomerService();
    },
    mounted() {
        this.customerService.getJobList().then((data) => {
            this.customers = data;
            this.loading = false;
        });

        FilterService.register(YOUR_FILTER, (value, filter) => {
            if (filter === undefined || filter === null || filter.trim() === '') {
                return true;
            }

            if (value === undefined || value === null) {
                return false;
            }

            return value.toString() === filter.toString();
        });
    },
    components: {
        FilterServiceDoc: FilterServiceDoc
    }
};
</script>
