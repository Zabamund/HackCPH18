import { Component, OnInit } from '@angular/core';
import { HttpServiceService } from '../shared';
import { stringify } from '@angular/compiler/src/util';

@Component({
  selector: 'grv-plot-a',
  templateUrl: './plot-a.component.html',
  styleUrls: ['./plot-a.component.css']
})
export class PlotAComponent implements OnInit {

  arg1 = 'John';
  arg2 = 'Doe';
  output = '';

  constructor(
    private httpService: HttpServiceService
  ) { }

  ngOnInit() {
  }

  displayData() {
    this.httpService.exampleAPICall(this.arg1, this.arg2)
    this.output = JSON.stringify(this.httpService.serverData)
  }

}
