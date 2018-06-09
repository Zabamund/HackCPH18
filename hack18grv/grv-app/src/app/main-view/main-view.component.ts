import { Component, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'grv-main-view',
  templateUrl: './main-view.component.html',
  styleUrls: ['./main-view.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class MainViewComponent implements OnInit {
  autoTicks = false;
  disabled = false;
  invert = false;
  max = 100;
  min = 0;
  showTicks = true;
  step = 1;
  thumbLabel = true;
  value = 0;
  vertical = false;

  get tickInterval(): number | 'auto' {
    return this.showTicks ? (this.autoTicks ? 'auto' : this._tickInterval) : 0;
  }
  set tickInterval(v) {
    this._tickInterval = Number(v);
  }
  private _tickInterval = 10;

  constructor() { }

  ngOnInit() {
  }

}
