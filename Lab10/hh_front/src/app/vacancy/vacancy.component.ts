import { Component } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {VacancyService} from "../vacancy.service";
import {Vacancy} from "../models";

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent {
  vacancies: Vacancy[] = [];
  id: number | undefined;
  newVacancy: string = '';
  newName: string = '';
  constructor(private route: ActivatedRoute, private vacancyService: VacancyService){

  }
  ngOnInit(): void{
    this.id = Number(this.route.snapshot.paramMap.get('id'));
    this.vacancyService.getVacanciesCompanies(this.id).subscribe((vacancies) => this.vacancies = vacancies);
  }
  addVacancy(){
    if (this.id)
      this.vacancyService.createVacancy(this.newVacancy, this.id).subscribe((vacancy) => {
        this.vacancies.push(vacancy)
        this.newVacancy = ''
      })
  }
  deleteVacancy(vacancy_id: number){
    this.vacancyService.deleteVacancy(vacancy_id).subscribe(() =>{
      this.vacancies = this.vacancies.filter((vacancy) => vacancy.id != vacancy_id);
    })
  }
  updateVacancy(vacancy_id: number){
    this.vacancyService.updateVacancy(vacancy_id, this.newName).subscribe((vacancy) => {
      this.vacancies.forEach((vacancy) =>{
          if (vacancy.id == vacancy_id){
            vacancy.name = this.newName
          }
        }
      );
      this.newName = ''
    })
  }
}
