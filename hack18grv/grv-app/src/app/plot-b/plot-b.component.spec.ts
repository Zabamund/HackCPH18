import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlotBComponent } from './plot-b.component';

describe('PlotBComponent', () => {
  let component: PlotBComponent;
  let fixture: ComponentFixture<PlotBComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlotBComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlotBComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
