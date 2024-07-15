'use client';
import React from 'react';
import {
  Button,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
} from '@nextui-org/react';

export default function TodoDetails({
  isOpen,
  onOpenChange,
  description,
  createdAt,
}: {
  isOpen: boolean;
  onOpenChange: () => void;
  description: string;
  createdAt: Date;
}) {
  return (
    <>
      <Modal isOpen={isOpen} onOpenChange={onOpenChange}>
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                Todo details
              </ModalHeader>
              <ModalBody>
                <p>{description}</p>
              </ModalBody>
              <ModalFooter>
                <Button color="primary" onPress={onClose}>
                  Ok
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}
