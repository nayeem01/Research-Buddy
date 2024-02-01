'use client'
import Image from 'next/image'
import React, { useEffect, useState } from 'react'
import { socketInitializer, socket } from './api/socket'

interface Message {
  body: string
  sender: string
  time: string
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([])
  const [mymessages, setMymessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const date = new Date()

  const sendMessage = () => {
    if (input) {
      socket.emit('message', {
        body: input,
        sender: 'me',
        time: `${date.getHours()}:${date.getMinutes()}`,
      })
      setMymessages((prevMessages) => [
        ...prevMessages,
        {
          body: input,
          sender: 'me',
          time: `${date.getHours()}:${date.getMinutes()}`,
        },
      ])
      setInput('')
    }
  }
  useEffect(() => {
    socketInitializer()
    socket.on('message', (message) => {
      setMessages((prevMessages) => [...prevMessages, message])
    })
  }, [])

  return (
    <main className="flex min-h-screen flex-col p-24">
      <div className="chat chat-start">
        <div className="chat-image avatar">
          <div className="w-10 rounded-full">
            <img
              alt="Tailwind CSS chat bubble component"
              src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg"
            />
          </div>
        </div>
        <div className="chat-header">
          Obi-Wan Kenobi
          <time className="text-xs opacity-50 pl-1">12:45</time>
        </div>

        <div className="chat-bubble chat-bubble-primary">
          What kind of nonsense is this
        </div>
      </div>

      {/* Chat ending  */}

      {mymessages.map((message, index) => (
        <div className="chat chat-end" key={index}>
          <div className="chat-image avatar">
            <div className="w-10 rounded-full">
              <Image
                alt="User avatar"
                src="/images/bot.jpg"
                width="64"
                height="64"
              />
            </div>
          </div>
          <div className="chat-header">
            {message.sender}
            <time className="text-xs opacity-50 pl-1">{message.time}</time>
          </div>
          <div className="chat-bubble chat-bubble-accent">{message.body}</div>
          <div className="chat-footer opacity-50">Seen at 12:46</div>
        </div>
      ))}

      {/* input */}
      <div className="flex">
        <input
          type="text"
          placeholder="Send a message"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="input input-bordered input-accent w-full xs"
        />
        <button
          className="btn btn-outline btn-accent ml-2"
          onClick={sendMessage}
        >
          Send
          <Image
            alt="User avatar"
            src="/images/send.svg"
            width="16"
            height="16"
          />
        </button>
      </div>
    </main>
  )
}
