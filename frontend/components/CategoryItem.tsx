import React from 'react';

export default function CategoryItem({
  title,
  icon,
}: {
  title: string;
  icon: React.ReactNode;
}) {
  return (
    <div className="flex w-full items-center gap-3 rounded-xl bg-white/20 p-2 shadow-sm transition duration-300 hover:scale-105 hover:cursor-pointer dark:bg-white/10">
      {icon}
      <p>{title}</p>
    </div>
  );
}
