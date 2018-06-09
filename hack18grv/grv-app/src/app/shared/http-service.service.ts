import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpServiceService {
  serverData: JSON;
  employeeData: JSON;

  constructor(private httpClient: HttpClient) { }

  // one call per backend end rest call
  // one backend rest call per function
  exampleAPICall() {
    this.httpClient.get('http://127.0.0.1:5002/API').subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData)
    })
  }

  sayHi() {
    this.httpClient.get('http://127.0.0.1:5002/').subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);
    })
  }

  getAllEmployees() {
    this.httpClient.get('http://127.0.0.1:5002/employees').subscribe(data => {
      this.employeeData = data as JSON;
      console.log(this.employeeData);
    })
  }
}
