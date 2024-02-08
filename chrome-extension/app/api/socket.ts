const socket = new WebSocket('ws://127.0.0.1:8000' + '/ws/chat/')

const socketInitializer = () => {
  socket.onopen = function (e) {
    console.log('Successfully connected to the WebSocket.')
  }
}

export { socket }
