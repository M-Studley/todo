import React from 'react';
import { Card, CardBody } from '@nextui-org/react';

export default function Todo() {
  return (
    <Card className="bg-white/40 dark:bg-white/40">
      <CardBody>
        <p>Todo item</p>
      </CardBody>
    </Card>
  );
}
