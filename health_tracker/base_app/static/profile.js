const app = new Vue({
    el: '#app',
    data: {
        events: [],
        users: [],
        user: {},
        points: 0,
        streak: 0
    }
})

// Needed for axios requests to work
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// Get userId from HTML
const userId = parseInt(document.getElementById('userId').value)

const resetDateTimeSelects = () => {
    const activitySelect = document.getElementById('activity')
    const dateSelect = document.getElementById('date')
    const timeSelect = document.getElementById('time')

    const now = Date.today().setTimeToNow()

    activitySelect.value = 'Exercise'
    dateSelect.value = now.toString('yyyy-MM-dd')
    timeSelect.value = now.toString('HH:mm')
}

const trackActivity = () => {
    const activitySelect = document.getElementById('activity')
    const dateSelect = document.getElementById('date')
    const timeSelect = document.getElementById('time')

    const activity = activitySelect.value
    const date = dateSelect.value
    const time = timeSelect.value

    axios.post('/events/', {
        withCredentials: true,
        'userId': userId,
        'activity_date': `${date} ${time}`,
        'activity': activity,
        'points': 50
    })
        .then((response) => {
            refreshData()
        })
        .catch((error) => {
            console.error(error)
        })
}

const refreshData = () => {
    // get users
    axios.get('/users/')
        .then((response) => {
            app.users = response.data
            app.user = response.data.find((user) => user.id === userId)
        })
        .catch((error) => {
            console.error(error)
        })

    // get events
    axios.get('/events/')
        .then((response) => {
            const eventsForUser = response.data.filter((event) => event.userId === userId)
            eventsForUser.forEach((event) => event.date = Date.parse(event.activity_date))
            app.events = eventsForUser.sort((a, b) => Date.compare(b.date, a.date))
            app.events.forEach((event) => event.date = Date.parse(event.activity_date))
            app.points = app.events.map((event) => event.points).reduce((a, b) => a + b, 0)
        })
        .catch((error) => {
            console.error(error)
        })
}

refreshData()
