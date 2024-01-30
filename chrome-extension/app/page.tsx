'use client'
import Image from 'next/image'
import React, { useEffect } from 'react'
// import io from 'socket.io-client'

// const socket = io(`http://localhost:5000`)

export default function Home() {
  useEffect(() => {
    // socket.on('receive_msg', () => {
    //   console.log('socket connection')
    // })
  }, [])
  return (
    <main className="flex min-h-screen flex-col justify-between p-24">
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
      <div className="chat chat-end">
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
          Anakin
          <time className="text-xs opacity-50 pl-1">12:46</time>
        </div>
        <div className="chat-bubble chat-bubble-accent">
          It's never happened before.
        </div>
        <div className="chat-footer opacity-50">Seen at 12:46</div>
      </div>
    </main>
  )
}
