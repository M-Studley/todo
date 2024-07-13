import React from 'react';
import { Avatar } from '@nextui-org/react';

export default function Todos() {
  return (
    <div className="grid h-[100vh] grid-cols-4 grid-rows-7 gap-2 bg-gradient-to-r from-indigo-200 via-purple-200 to-pink-200">
      <nav className="row-span-7 m-3 rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 p-6 shadow-xl backdrop-blur-xl">
        1
      </nav>
      <header className="col-span-3 row-span-1 ml-3 mr-3 mt-3 flex items-center justify-between rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 p-8 shadow-lg backdrop-blur-lg">
        <h2 className="text-2xl">Hi, John!</h2>
        <Avatar
          className="ml-auto"
          src="https://i.pravatar.cc/150?u=a042581f4e29026024d"
        />
      </header>
      <main className="col-span-3 col-start-2 row-span-7 row-start-2 m-3 mb-4 rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 p-6 shadow-xl backdrop-blur-lg">
        3
      </main>
    </div>
  );
}
