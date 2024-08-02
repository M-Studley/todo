import React from 'react';
import { Cog6ToothIcon } from '@heroicons/react/24/outline';
import { Avatar } from '@nextui-org/react';
import dynamic from 'next/dynamic';

import Sidebar from '@/components/Sidebar';

import ThemeSwitcher from '../../components/ThemeSwitcher';
import { TodoData } from '../../components/Todo';

const Todo = dynamic(() => import('../../components/Todo'), { ssr: false });

export default async function TodosPage() {
  const response = await fetch('http://localhost:3000/mockup-todos.json', {
    cache: 'no-cache',
  });
  const todos: TodoData[] = await response.json();

  return (
    <div className="grid h-[100vh] grid-cols-4 grid-rows-7 gap-2 bg-gradient-to-r from-indigo-300 via-purple-300 to-pink-300 dark:from-indigo-700 dark:via-purple-700 dark:to-pink-700">
      <Sidebar />
      <header className="col-span-3 row-span-1 ml-3 mr-3 mt-3 flex items-center justify-between rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 p-8 shadow-lg backdrop-blur-xl dark:border-0 dark:bg-black/20">
        <h2 className="text-2xl italic">Hi,&nbsp;</h2>
        <h2 className="text-2xl">John</h2>
        <div className="ml-auto flex items-center gap-2">
          <ThemeSwitcher />
          {
            // known bug of the "avatar" component causing disableAnimation warning on browser console.
            // will be fixed in the next version of NextUI. GitHub issue ref: https://github.com/nextui-org/nextui/issues/3257
          }
          <Avatar src="https://i.pravatar.cc/150?u=a042581f4e29026024d" />
        </div>
      </header>
      <main className="col-span-3 col-start-2 row-span-7 row-start-2 m-3 mb-4 flex flex-col gap-4 rounded-xl border border-white border-opacity-20 bg-white bg-opacity-30 px-8 py-10 shadow-xl backdrop-blur-xl dark:border-0 dark:bg-black/20">
        <div className="mb-4 flex">
          <h2 className="text-xl">Category</h2>
          <Cog6ToothIcon className="ml-auto" width={24} />
        </div>
        {todos.map((todo) => {
          return (
            <Todo
              key={todo.id}
              id={todo.id}
              name={todo.name}
              description={todo.description}
              category={todo.category}
              priority={todo.priority}
              createdAt={new Date(todo.createdAt)}
              deadline={todo.deadline && new Date(todo.deadline)}
              completed={todo.completed}
            />
          );
        })}
      </main>
    </div>
  );
}
