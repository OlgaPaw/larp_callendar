<template>
  <div id="cal-holder">
    <calendar-view
			:show-date="showDate"
			class="theme-default"
      :events="events"
    >
			<calendar-view-header
				slot="header"
				slot-scope="t"
				:header-props="t.headerProps"
				@input="setShowDate"
        />
		</calendar-view>
  </div>
</template>

<script>
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar"
import axios from 'axios'

require("vue-simple-calendar/static/css/default.css")
require("vue-simple-calendar/static/css/holidays-us.css")

export default {
  name: 'Calendar',
	components: {
		CalendarView,
		CalendarViewHeader,
	},
	data() {
		return {
			/* Show the current month, and give it some fake events to show */
			showDate: this.thisMonth(1),
			startingDayOfWeek: 0,
			displayPeriodUom: "month",
			displayPeriodCount: 1,
			showEventTimes: true,
			useDefaultTheme: true,
      events: [],
		}
	},
	computed: {
		themeClasses() {
			return {
				"theme-default": this.useDefaultTheme
			}
		},
  },
  async mounted () {
    const response = await axios.get('http://localhost:8000/api/larps/')
      .catch(err => console.error(err))
    this.events = response.data.map(x => ({
      title: x.name,
      startDate: x.date_start,
      endDate: x.date_end,
    }))
  },
	methods: {
		thisMonth(d, h, m) {
			const t = new Date()
			return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0)
		},
		setShowDate(d) {
			this.showDate = d
		},
	},
}
</script>

<style>
#cal-holder {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  height: 100%;
}
</style>