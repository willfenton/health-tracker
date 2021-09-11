axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const activitySelect = document.getElementById('activity')
const dateSelect = document.getElementById('date')
const timeSelect = document.getElementById('time')

const resetDateTimeSelects = () => {
    activitySelect.value = "Exercise"

    const now = new Date()
    const date = now.getFullYear() + "-" + ("0" + (now.getMonth() + 1)).slice(-2) + "-" + ("0" + now.getDate()).slice(-2)
    const time = ("0" + now.getHours()).slice(-2) + ":" + ("0" + now.getMinutes()).slice(-2)

    dateSelect.value = date
    timeSelect.value = time
}

const userId = document.getElementById('userId').value

const trackActivity = () => {
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
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}

