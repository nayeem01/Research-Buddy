import express from 'express'
import dotenv from 'dotenv'
import { createServer } from 'node:http'
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'
import { Server } from 'socket.io'

dotenv.config()

const app = express()
const server = createServer(app)
const io = new Server(server)

app.get('/', (req, res) => {
  res.send('<h1>hello </h1>')
})

io.on('connection', (socket) => {
  console.log('connection=======================')
})

const port = process.env.PORT
const url = process.env.URL

server.listen(port, () => {
  console.log(`server running at http://${url}:${port}`)
})
