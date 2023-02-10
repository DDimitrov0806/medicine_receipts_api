import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ReceiptComponent } from './components/receipts/receipt.component';

const routes: Routes = [
  { path: '', redirectTo: 'receipts', pathMatch: 'full'},
  { path: 'receipts', component: ReceiptComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
