import React from 'react';

type PriorityType = 'low' | 'neutral' | 'high' | 'critical';

export default function Priority({ priority }: { priority: PriorityType }) {
  const getColorClass = (priority: PriorityType) => {
    switch (priority) {
      case 'low':
        return 'text-green-400';
      case 'neutral':
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
