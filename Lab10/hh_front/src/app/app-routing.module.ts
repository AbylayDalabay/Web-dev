import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {VacancyComponent} from "./vacancy/vacancy.component";
import {CompanyComponent} from "./company/company.component";

const routes: Routes = [
  {path: '', component: CompanyComponent},
  {path: ':id/vacancies', component: VacancyComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
