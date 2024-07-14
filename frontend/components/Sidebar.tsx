import React from 'react';
import {
  BuildingStorefrontIcon,
  GlobeEuropeAfricaIcon,
  HomeIcon,
} from '@heroicons/react/24/outline';

export default function Sidebar() {
  return (
    <nav className="m-3rounded-xl row-span-7 border border-white border-opacity-20 bg-white bg-opacity-30 p-6 shadow-xl backdrop-blur-xl">
      <h1 className="mb-12 text-2xl">Todo App</h1>
      <section className="flex flex-col gap-4">
        <div className="flex w-full items-center gap-3 rounded-xl bg-white/10 p-2 shadow-sm">
          <HomeIcon width={22} />
          <p>All</p>
        </div>
        <div className="flex w-full items-center gap-3 rounded-xl bg-white/10 p-2 shadow-sm">
          <BuildingStorefrontIcon width={22} />
          <p>Groceries</p>
        </div>
        <div className="flex w-full items-center gap-3 rounded-xl bg-white/10 p-2 shadow-sm">
          <GlobeEuropeAfricaIcon width={22} />
          <p>Travels</p>
        </div>
      </section>
    </nav>
  );
}
