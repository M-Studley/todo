import type { Metadata } from 'next';
import { Libre_Franklin } from 'next/font/google';
import { Toaster } from 'sonner';

import { Providers } from './providers';

import './globals.css';

const libre = Libre_Franklin({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Todo App',
  description: 'Frontend for the Todo App project',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${libre.className} scroll-smooth bg-background bg-gradient-to-b from-slate-50 to-slate-200 dark:bg-gradient-to-b dark:from-gray-600/40 dark:to-gray-700/60`}
      >
        <Toaster richColors position="top-center" />
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
