import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Vacancy} from "./models";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  BASE_URL = 'http://127.0.0.1:8000'
  id: number | undefined;
  constructor(private client: HttpClient) {}
  ngOnInit(): void{
  }
  getVacancies(): Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/vacancies`)
  }
  getVacanciesCompanies(id:number): Observable<Vacancy[]>{
    this.id = id;
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies`)
  }
  createVacancy(vacancyName: string, id: number): Observable<Vacancy>{
    return this.client.post<Vacancy>(
      `${this.BASE_URL}/api/vacancies/`,
      {name: vacancyName,
        company:id}
    )
  }
  deleteVacancy(vacancy_id: number): Observable<any>{
    return this.client.delete<any>(
      `${this.BASE_URL}/api/vacancies/${vacancy_id}/`
    )
  }
  updateVacancy(vacancy_id: number, vacancyName: string): Observable<Vacancy>{
    return this.client.put<Vacancy>(
      `${this.BASE_URL}/api/vacancies/${vacancy_id}/`,
      {name: vacancyName}
    )
  }
}
