import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from 'src/app/models'
import { VacancyService } from './vacancy.service';
import { CompanyService } from './company.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'hh_front';

}
