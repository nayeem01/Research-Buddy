import io from 'socket.io-client'
const socket = io(`http://localhost:5000`)

const socketInitializer = async () => {
  socket.on('connect', () => {
    console.log('connected')
  })
}

export { socketInitializer, socket }
