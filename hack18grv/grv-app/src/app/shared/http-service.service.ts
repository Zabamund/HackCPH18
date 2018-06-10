import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpServiceService {
  serverData: JSON;
  employeeData: JSON;

  constructor(public httpClient: HttpClient) { }

  // one call per backend end rest call
  // one backend rest call per function
  exampleAPICall(arg1:string, arg2:string) {
    // Initialize Params Object
    let Params = new HttpParams();

    // Begin assigning parameters
    //Params = Params.append('arg1', 'John Doe');
    //Params = Params.append('arg2', 'Jane Doe');
    Params = Params.append('arg1', arg1);
    Params = Params.append('arg2', arg2);

    // Make the API call using the new parameters.
    this.httpClient.get('http://127.0.0.1:5002/API', {
      params: Params
    }).subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData)
      return this.serverData
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
