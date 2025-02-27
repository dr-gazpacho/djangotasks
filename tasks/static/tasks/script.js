console.log('working');

async function newFetch() {
    try {
        const response = await fetch('/tasks/api/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log('Error:', error.message);
    }
}

newFetch();