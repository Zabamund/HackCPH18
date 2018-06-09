import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlotAComponent } from './plot-a.component';

describe('PlotAComponent', () => {
  let component: PlotAComponent;
  let fixture: ComponentFixture<PlotAComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlotAComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlotAComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
