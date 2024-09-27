'use client';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Junta } from '@/types/junta';
import { DollarSignIcon, UserIcon } from 'lucide-react';

export function JuntaCard({ junta, onSelectJunta, onDeleteJunta }: { junta: Junta; onSelectJunta: (junta: Junta) => void; onDeleteJunta: (juntaId: number) => void }) {
  const totalSavings = junta.total_shares * junta.share_value;
  const progress = (junta.current_month / junta.duration_months) * 100;
  return (
    <Card className="w-full">
      <CardHeader>
        <CardTitle>{junta.name}</CardTitle>
        <CardDescription>Duración: {junta.duration_months} meses</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="flex justify-between items-center">
            <span className="flex items-center">Capital Social: S/.{totalSavings}</span>
            <span className="flex items-center"><UserIcon className="mr-2 h-4 w-4" />{junta.members.length} socios</span>
          </div>
          <Progress value={progress} className="w-full" />
          <p>Mes actual: {junta.current_month} de {junta.duration_months}</p>
        </div>
      </CardContent>
      <CardFooter className="flex justify-between">
        <Button onClick={() => onSelectJunta(junta)} className="flex-1 mr-2">Ver detalles</Button>
        <Button variant="destructive" onClick={() => onDeleteJunta(junta.id)} className="flex-1 ml-2">Eliminar</Button>
      </CardFooter>
    </Card>
  )
}