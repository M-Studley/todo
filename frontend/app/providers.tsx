import { NextUIProvider } from '@nextui-org/react';
import { ThemeProvider } from 'next-themes';

export async function Providers({ children }: { children: React.ReactNode }) {
  return (
    <NextUIProvider>
      <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
        {children}
      </ThemeProvider>
    </NextUIProvider>
  );
}
