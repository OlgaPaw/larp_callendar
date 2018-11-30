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
			events: [
				{
					id: "e3",
					startDate: this.thisMonth(7, 9, 25),
					endDate: this.thisMonth(10, 16, 30),
					title: "Multi-day event with a long title and times",
				},
				{
					id: "e4",
					startDate: this.thisMonth(20),
					title: "My Birthday!",
					classes: "birthday",
					url: "https://en.wikipedia.org/wiki/Birthday",
				},
				{
					id: "e5",
					startDate: this.thisMonth(5),
					endDate: this.thisMonth(12),
					title: "Multi-day event",
					classes: "purple",
				}
			],
		}
	},
	computed: {
		themeClasses() {
			return {
				"theme-default": this.useDefaultTheme
			}
		},
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