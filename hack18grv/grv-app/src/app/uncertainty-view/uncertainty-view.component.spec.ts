import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UncertaintyViewComponent } from './uncertainty-view.component';

describe('UncertaintyViewComponent', () => {
  let component: UncertaintyViewComponent;
  let fixture: ComponentFixture<UncertaintyViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UncertaintyViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UncertaintyViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
