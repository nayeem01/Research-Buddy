import express from 'express'
import dotenv from 'dotenv'
import { createServer } from 'http'
// import cors from 'cors'
import { Server } from 'socket.io'

dotenv.config()

const app = express()
const httpServer = createServer()

const io = new Server(httpServer, {
  cors: {
    origin: process.env.CLIENT_URL
  }
})

app.get('/', (req, res) => {
  res.send('<h1>hello </h1>')
})

io.on('connection', (socket) => {
  console.log(`connection======================= ${socket.id}`)
  socket.on('message', (msg) => {
    console.log('message: ' + msg)
  })
})

const port = process.env.PORT
const url = process.env.URL

httpServer.listen(port, () => {
  console.log(`server running at http://${url}:${port}`)
})
