import React from 'react';

export default function Priority({
  priority,
}: {
  priority: 'low' | 'normal' | 'high' | 'critical';
}) {
  const getColorClass = (priority: 'low' | 'normal' | 'high' | 'critical') => {
    switch (priority) {
      case 'low':
        return 'text-green-400';
      case 'normal':
        return 'text-blue-400 dark:text-blue-500';
      case 'high':
        return 'text-yellow-400';
      case 'critical':
        return 'text-red-400';
      default:
        return 'text-gray-400';
    }
  };

  return (
    <p className={`text-lg font-semibold ${getColorClass(priority)}`}>!</p>
  );
}
