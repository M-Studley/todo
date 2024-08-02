import React from 'react';
import { Tooltip } from '@nextui-org/react';

type PriorityType = 'low' | 'neutral' | 'high' | 'critical';

export default function Priority({ priority }: { priority: PriorityType }) {
  const getNameAndColor = (priority: PriorityType) => {
    switch (priority) {
      case 'low':
        return { name: 'Low', color: 'text-green-400' };
      case 'neutral':
        return { name: 'Neutral', color: 'text-blue-400 dark:text-blue-500' };
      case 'high':
        return { name: 'High', color: 'text-yellow-400' };
      case 'critical':
        return { name: 'Critical', color: 'text-red-400' };
      default:
        return { name: 'Unknown', color: 'text-gray-400' };
    }
  };

  const currentPriority = getNameAndColor(priority);

  return (
    <Tooltip content={currentPriority.name} className="bg-opacity-60">
      <p
        className={`cursor-default text-lg font-semibold ${currentPriority.color}`}
      >
        !
      </p>
    </Tooltip>
  );
}
