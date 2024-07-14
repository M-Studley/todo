import React from 'react';
import {
  BuildingStorefrontIcon,
  GlobeEuropeAfricaIcon,
  HomeIcon,
} from '@heroicons/react/24/outline';

import CategoryItem from './CategoryItem';

export default function Sidebar() {
  return (
    <nav className="m-3rounded-xl row-span-7 border border-white border-opacity-20 bg-white bg-opacity-30 p-6 shadow-xl backdrop-blur-xl">
      <h1 className="mb-12 text-2xl">Todo App</h1>
      <section className="flex flex-col gap-4">
        <CategoryItem title="All" icon={<HomeIcon width={22} />} />
        <CategoryItem
          title="Groceries"
          icon={<BuildingStorefrontIcon width={22} />}
        />
        <CategoryItem
          title="Travels"
          icon={<GlobeEuropeAfricaIcon width={22} />}
        />
      </section>
    </nav>
  );
}
