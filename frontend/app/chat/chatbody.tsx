'use client'
import Image from 'next/image'
import React, { useState, useEffect } from 'react'
import { useGlobalContext } from '../Context/store'
import { socket } from '../lib/socket'
interface Message {
  body: string
  sender: string
  time: string
}

export default function ChatBody() {
  const { data, setData } = useGlobalContext()
  const [mymessages, setMymessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const date = new Date()

  const sendMessage = () => {
    if (input) {
      socket.send(
        JSON.stringify({
          message: {
            body: input,
            sender: 'me',
            time: `${date.getHours()}:${date.getMinutes()}`,
          },
        })
      )

      setInput('')
    }
  }

  const handleKeyboardEvent = (event: any) => {
    if (event.key === 'Enter') sendMessage()
  }
  socket.onmessage = function (event) {
    const msData = JSON.parse(event.data)
    setMymessages((prevMessages) => [...prevMessages, msData.message])
  }

  return (
    <div className="drawer-content flex flex-col ">
      <main className="flex-1 overflow-y-auto md:pt-4 pt-4 px-6  bg-base-200">
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
                  src="/assets/bot.jpg"
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
          </div>
        ))}

        {/* input */}
        <div className="flex join">
          {input.toLowerCase().startsWith('llm') && (
            <div className="badge badge-info gap-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                className="inline-block w-4 h-4 stroke-current"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M6 18L18 6M6 6l12 12"
                ></path>
              </svg>
              LLM
            </div>
          )}
          <input
            type="text"
            placeholder="Send a message"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="input input-bordered input-accent w-full xs"
            onKeyDown={handleKeyboardEvent}
          />
          <button
            className="btn btn-outline btn-accent ml-2"
            onClick={sendMessage}
          >
            Send
            <Image
              alt="User avatar"
              src="/assets/send.svg"
              width="16"
              height="16"
            />
          </button>
        </div>
      </main>
    </div>
  )
}
