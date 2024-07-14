import React from 'react';
import { Cog6ToothIcon } from '@heroicons/react/24/outline';
import { Avatar } from '@nextui-org/react';

import ThemeSwitcher from '../../components/ThemeSwitcher';
import Todo from '../../components/Todo';

export default function TodosPage() {
  return (
    <div className="grid h-[100vh] grid-cols-4 grid-rows-7 gap-2 bg-gradient-to-r from-indigo-300 via-purple-300 to-pink-300 dark:from-indigo-700 dark:via-purple-700 dark:to-pink-700">
      <nav className="row-span-7 m-3 rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 p-6 shadow-xl backdrop-blur-xl">
        1
      </nav>
      <header className="col-span-3 row-span-1 ml-3 mr-3 mt-3 flex items-center justify-between rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 p-8 shadow-lg backdrop-blur-lg">
        <h2 className="text-2xl">Hi, John!</h2>
        <div className="ml-auto flex items-center gap-2">
          <ThemeSwitcher />
          <Avatar src="https://i.pravatar.cc/150?u=a042581f4e29026024d" />
        </div>
      </header>
      <main className="col-span-3 col-start-2 row-span-7 row-start-2 m-3 mb-4 flex flex-col gap-4 rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 px-8 py-10 shadow-xl backdrop-blur-lg">
        <div className="mb-4 flex">
          <h2 className="text-xl">Category</h2>
          <Cog6ToothIcon className="ml-auto" width={24} />
        </div>
        <Todo
          title="Test"
          status="completed"
          priority="critical"
          date={new Date()}
        />
        <Todo
          title="Test 2"
          status="completed"
          priority="normal"
          date={new Date()}
        />
        <Todo
          title="Test 3"
          status="not completed"
          priority="low"
          date={new Date()}
        />
        <Todo
          title="Test 3"
          status="not completed"
          priority="high"
          date={new Date()}
        />
      </main>
    </div>
  );
}
