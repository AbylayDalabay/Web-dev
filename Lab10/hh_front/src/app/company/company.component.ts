import { Component } from '@angular/core';
import {CompanyService} from "../company.service";
import {Company} from "../models";

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent {
  companies: Company[] = [];
  newCompany: string = '';
  newName: string = '';
  constructor(private companyService: CompanyService){

  }
  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((companies) => {
      this.companies = companies;
    })
  }
  addCompany(){
    this.companyService.createCompany(this.newCompany).subscribe((company) => {
      this.companies.push(company)
      this.newCompany = ''
    })
  }
  deleteCompany(company_id: number){
    this.companyService.deleteCompany(company_id).subscribe((data) =>{
      this.companies = this.companies.filter((company) => company.id != company_id);
    })
  }
  updateCompany(company_id: number){
    this.companyService.updateCompany(company_id, this.newName).subscribe((company) => {
      this.companies.forEach((company) =>{
          if (company.id == company_id){
            company.name = this.newName
          }
        }
      );
      this.newName = ''
    })
  }
}
